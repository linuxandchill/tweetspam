defmodule GetTweets do
  def get_user do 
    user = ExTwitter.user_timeline(screen_name: "_pivx", count: 2)
  end
end
