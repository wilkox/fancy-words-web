class TextsController < ApplicationController

  def new
    @text = Text.new
  end

  def create
    @text = Text.new(params[:text])
    if @text.save
      redirect_to @text
    else
      redirect_to root_path
    end
  end

  def show
    @text = Text.find(params[:id])
  end
end
