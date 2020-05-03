describe 'Pachorra':
  it 'ya no entiende firmar_contrato!':
    expect(Pachorra).not_to respond_to :firmar_contrato!


  it 'entiende ave=':
    expect(Pachorra).to respond_to :ave=


  it 'firma contrato con Pepita y la entrena':
    Pachorra.ave = Pepita
    Pachorra.entrenar_ave!
    expect(Pepita.energia).to eq 1250


  it 'firma contrato con Pepo y lo entrena':
    Pachorra.ave = Pepo
    Pachorra.entrenar_ave!
    expect(Pepo.energia).to eq 1000

