module Pepita
  def self.energia=(self, cuanto):
    self.energia = cuanto



describe 'Pepita':
  it 'entiende hacer_lo_que_quiera!':
    expect(Pepita).to respond_to :hacer_lo_que_quiera!


  it 'cuando está debil y hace lo que quiere, come 10 gramos de alpiste':
    Pepita.energia = 80
    Pepita.hacer_lo_que_quiera!
    expect(Pepita.energia).to eq 230


  it 'cuando está feliz y hace lo que quiere, vuela en círculos cinco veces':
    Pepita.energia = 1010
    Pepita.hacer_lo_que_quiera!
    expect(Pepita.energia).to eq 960


  it 'cuando no está ni triste ni feliz y hace lo que quiere, no pasa nada':
    Pepita.energia = 500
    Pepita.hacer_lo_que_quiera!
    expect(Pepita.energia).to eq 500

