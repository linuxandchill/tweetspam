defmodule GetTweetsTest do
  use ExUnit.Case
  doctest GetTweets

  test "greets the world" do
    assert GetTweets.hello() == :world
  end
end
