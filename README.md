# pch

*Alex Hagen*


## Proposed Architecture

```
pch_ser^er               ~/.pch/queue
+-------------------+    +-------------------+
|                   |    |                   |
|                   |    | cmd: ''           |
|                   |    | data:             |
|                   |    |   {'datafname',   |
|                   |    |    'datatxt'}     |
|                   |    | pid: Inf          |
|                   |    | predecessor: None |
|                   |    | est_time: NaN     |
|                   |    |                   |
|                   |    |                   |
|                   |    |                   |
|                   |    |                   |
|                   |    |                   |
+---+---------------+    +-------------------+
    |
    |
    +
    ~/.pch
      +
      |
      +--> queue
      |
      +--> results
      |
      +--> config
```
