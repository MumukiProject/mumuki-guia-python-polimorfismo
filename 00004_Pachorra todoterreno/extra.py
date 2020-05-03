module Pepita
  self.energia = 1000

  def self.energi(self):
    self.energia


  def self.volar_en_circulos!
    self.energia -= 10


  def self.comer_alpiste!(self, gramos):
    self.energia += gramos * 15


  def self.debil?
    self.energia < 100


  def self.feliz?
    self.energia > 1000


  def self.hacer_lo_que_quiera!
    if self.debil?
      self.comer_alpiste!(10)


    if self.feliz?
      5.times { self.volar_en_circulos! }




module Pepo
  self.energia = 1000

  def self.energi(self):
    self.energia


  def self.volar_en_circulos!
    if self.pesado?
      self.energia -= 15
    else
      self.energia -= 5



  def self.comer_alpiste!(self, gramos):
    self.energia += gramos / 2


  def self.pesado?
    self.energia > 1100


  def self.hacer_lo_que_quiera!
    self.comer_alpiste!(120)

