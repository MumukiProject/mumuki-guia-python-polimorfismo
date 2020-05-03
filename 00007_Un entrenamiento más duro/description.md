Analicemos el error:

```python
ム Pachorra.entrenar_ave!
undefined method `hacer_lo_que_quiera!' for Norita:Module (NoMethodError)
```

En criollo, lo que dice ahí es que `Norita` no entiende el mensaje `hacer_lo_que_quiera!`, y por eso `Pachorra` no la puede entrenar; este mensaje forma parte de su rutina.

Miremos ahora el método `entrenar_ave!` de `Emilce`, una entrenadora un poco más estricta:

```python
module Emilce
  def self.entrenar_ave!
    53.times { self.ave.volar_en_circulos! }
    self.ave.comer_alpiste!(8)


```

> ¿Podrá `Norita` entrenar con `Emilce`? ¿Y `Pepita`? ¿Y `Pepo`?
>
> Probalo en la consola y completá el código con `True` (verdadero) o `False` (falso) según corresponda para cada ave.
