from typing import TextIO
from time import time
import keras
import tensorflow as tf
import demetric as dm
from checkptr import Checkpointer
import moveread.ocr as mo

def loop(
  model: keras.Model, train_ds: tf.data.Dataset, *,
  val_ds: tf.data.Dataset, opt: keras.optimizers.Optimizer, 
  logger: dm.Metrics, checkpt: Checkpointer, logstream: TextIO | None = None,
  metrics_freq: int = 10, n_batches: int | None = None, epochs: int = 10,
  n_val_batches: int | None = None
):
  
  train_step = mo.compile_train(model, opt)
  evaluate, metrics_step = mo.compile_val(model, n_val_batches)

  running_loss = 0.
  t0 = time()
  i = 0
  n = 0
  history: list[dict[str, float]] = []
  
  if logstream:
    print('Baseline evaluation...', file=logstream)
  val_metrics = evaluate(val_ds, logstream=logstream)
  val_metrics = { f'val_{k}': v for k, v in val_metrics.items() }
  history.append(val_metrics)
  logger.log(val_metrics, step=-1)
  display = ' - '.join([f'{k}: {v:.3f}' for k, v in val_metrics.items()])

  for epoch in range(epochs):
    t_epoch = time()
    for i, (x, y) in enumerate(train_ds):
      losses, z = train_step((x, y))
      loss = tf.reduce_mean(losses)
      running_loss += loss

      if i % metrics_freq == 0:
        t1 = time()
        batch_time = (t1-t0) / metrics_freq
        t0 = t1

        batch_metrics = metrics_step(y, z)
        if logstream:
          display = ' - '.join([f'{k}: {v:.3f}' for k, v in batch_metrics.items()])
          msg = f'epoch {epoch} - {i} / {n_batches or "UNK"} - loss {float(loss):.3f} - {1e3*batch_time:.1f} ms/batch - {t1-t_epoch:.1f} secs elapsed - {display}',
          n_val_batches: int | None = None
          print(f'\r{msg}\t\t', end='', file=logstream, flush=True)

        step = n + i
        logger.log({'loss': float(loss), **batch_metrics}, step=step)

      if tf.math.is_nan(loss):
        print(f'WARNING: Loss is NaN at {i}', file=logstream)

    checkpt.checkpoint(model, f'{epoch}.weights.h5')
    val_metrics = evaluate(val_ds, logstream=logstream)
    val_metrics = { f'val_{k}': v for k, v in val_metrics.items() }
    history.append(val_metrics)
    logger.log(val_metrics, step=epoch)

    n += i

  return history