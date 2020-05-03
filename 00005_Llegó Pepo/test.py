module Pepo
  def self.energia=(self, valor):
    self.energia = valor



describe 'Pepo':
  before(:each) { Pepo.energia = 1000 }

  it 'existe':
    expect(Pepo).to be


  it 'gana 25 de energía cuando come 50 gramos de alpiste':
    Pepo.comer_alpiste!(50)
    expect(Pepo.energia).to eq 1025


  it 'gana 30 de energía cuando come 60 gramos de alpiste':
    Pepo.comer_alpiste!(60)
    expect(Pepo.energia).to eq 1030


  it 'gasta 15 de energía cuando vuela y está pesado':
    Pepo.energia = 1200
    Pepo.volar_en_circulos!
    expect(Pepo.energia).to eq 1185


  it 'gasta 5 de energía cuando vuela y no está pesado':
    Pepo.volar_en_circulos!
    expect(Pepo.energia).to eq 995


  it 'come 120 gramos de alpiste cuando hace lo que quiere':
    Pepo.hacer_lo_que_quiera!
    expect(Pepo.energia).to eq 1060

