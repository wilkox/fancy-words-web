class AddIndexToTexts < ActiveRecord::Migration
  def self.up
    add_index :texts, :content
  end

  def self.down
  end
end
