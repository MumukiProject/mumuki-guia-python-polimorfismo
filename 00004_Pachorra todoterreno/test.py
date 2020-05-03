module Pepo
  self.energia = 900


describe 'Pachorra':
  it 'entiende firmar_contrato!':
    expect(Pachorra).to respond_to :firmar_contrato!


  it 'firma contrato con Pepita y la entrena':
    Pachorra.firmar_contrato!(Pepita)
    Pachorra.entrenar_ave!
    expect(Pepita.energia).to eq 1250


  it 'firma contrato con Pepo y lo entrena':
    Pachorra.firmar_contrato!(Pepo)
    Pachorra.entrenar_ave!
    expect(Pepo.energia).to eq 900

