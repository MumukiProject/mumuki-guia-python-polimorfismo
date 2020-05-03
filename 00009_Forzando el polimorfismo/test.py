describe 'Norita':
  it 'entiende hacer_lo_que_quiera!':
    expect(Norita).to respond_to :hacer_lo_que_quiera!


  it 'no hace nada cuando hace lo que quiere':
    Norita.hacer_lo_que_quiera!
    expect(Norita.energia).to eq 500


  it 'puede entrenar con Pachorra':
    Pachorra.firmar_contrato!(Norita)
    Pachorra.entrenar_ave!
    expect(Norita.energia).to eq 20

