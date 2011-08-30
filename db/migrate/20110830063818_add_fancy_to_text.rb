class AddFancyToText < ActiveRecord::Migration
  def self.up
    add_column :texts, :fancy, :string
  end

  def self.down
  end
end
