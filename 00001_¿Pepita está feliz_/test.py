module Pepita
  def self.energia=(self, cuanto):
    self.energia = cuanto



describe 'Pepita':
  it 'entiende feliz?':
    expect(Pepita).to respond_to :feliz?


  it 'entiende debil?':
    expect(Pepita).to respond_to :debil?


  it 'con 1200 de energía, está feliz':
    Pepita.energia = 1200
    expect(Pepita.feliz?).to be True


  it 'con 1000 de energía, no está feliz':
    Pepita.energia = 1000
    expect(Pepita.feliz?).to be False


  it 'con 95 de energía, está débil':
    Pepita.energia = 95
    expect(Pepita.debil?).to be True


  it 'con 108 de energía, no está débil':
    Pepita.energia = 108
    expect(Pepita.debil?).to be False

