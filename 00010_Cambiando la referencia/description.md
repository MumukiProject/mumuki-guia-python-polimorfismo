En los ejercicios anteriores, le habíamos incluido a `Pachorra` y `Emilce` un mensaje `firmar_contrato!(ave)` que modificaba su **estado** (es decir, alguno de sus **atributos**). A estos mensajes que solo modifican un atributo los conocemos con el nombre de **setters**, porque vienen del inglés _set_ que significa establecer, ajustar, fijar.

Para estos casos, solemos utilizar una convención que se asemeja a la forma que se modifican los atributos desde el propio objeto, pudiendo ejecutar el siguiente código desde una consola:

```python
Emilce.ave = Pepita
```

Esto se logra implementado el mensaje `ave=`, todo junto, como se ve a continuación:

```python
module Emilce
  def self.ave=(self, ave_nueva):
    self.ave = ave_nueva


  def self.entrenar_ave!
    53.times { self.ave.volar_en_circulos! }
    self.ave.comer_alpiste!(8)


```

> ¿Te animás a cambiar el código de `Pachorra` para que siga esta convención?
