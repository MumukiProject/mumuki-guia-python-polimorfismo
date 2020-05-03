module Pachorra
  def self.firmar_contrato!(self, un_ave):
    self.ave = un_ave


  def self.entrenar_ave!
    10.times { self.ave.volar_en_circulos! }
    self.ave.comer_alpiste! 30
    5.times { self.ave.volar_en_circulos! }
    self.ave.hacer_lo_que_quiera!

