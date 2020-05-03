describe 'Pachorra':
  it 'existe':
    expect(Pachorra).to be


  it 'entiende el mensaje entrenar_ave!':
    expect(Pachorra).to respond_to :entrenar_ave!


  it 'hace entrenar a Pepita cuando recibe entrenar_ave!':
    Pachorra.entrenar_ave!
    expect(Pepita.energia).to eq 1250

