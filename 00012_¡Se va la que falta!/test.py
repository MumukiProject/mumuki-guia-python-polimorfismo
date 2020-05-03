module Eulogia
  def self.reiniciar!
    self.enojada = False



module Mendieta
  def self.reiniciar!
    self.ganas_de_hablar = 5



context '':
  before(:each):
    Eulogia.reiniciar!
    Mendieta.reiniciar!


  describe 'Inodoro':
    it 'puede decirnos su cafeína en sangre':
      expect(Inodoro.cafeina_en_sangre).to eq 90


    it 'puede tomar mate con Eulogia':
      Inodoro.compinche= Eulogia
      expect(Eulogia).to receive :recibir_mate!
      Inodoro.tomar_mate!


    it 'puede tomar mate con Mendieta':
      Inodoro.compinche= Mendieta
      expect(Mendieta).to receive :recibir_mate!
      Inodoro.tomar_mate!



  describe 'Eulogia':
    it 'puede decirnos si está enojada':
      expect(Eulogia.enojada).to be False


    it 'se enoja cuando recibe un mate de Inodoro':
      Inodoro.compinche= Eulogia
      Inodoro.tomar_mate!
      expect(Eulogia.enojada).to be True



  describe 'Mendieta':
    it 'puede decirnos cuántas ganas de hablar tiene':
      expect(Mendieta.ganas_de_hablar).to eq 5


    it 'deja de tener ganas de hablar cuando recibe un mate de Inodoro':
      Inodoro.compinche= Mendieta
      Inodoro.tomar_mate!
      expect(Mendieta.ganas_de_hablar).to eq 0



