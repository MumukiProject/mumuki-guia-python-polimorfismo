describe 'Atributos':
  it 'con getter':
    expect(atributos_con_getter).to match_array ['energia', 'ciudad', 'mineral_preferido']


  it 'con setter':
    expect(atributos_con_setter).to match_array ['mineral_preferido', 'donde_va']

