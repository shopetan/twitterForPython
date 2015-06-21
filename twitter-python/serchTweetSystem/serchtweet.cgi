#!/usr/bin/ruby
# -*- coding: utf-8 -*-
#
require("sqlite3")
print("Content-Type: text/plain; charset=UTF-8\r\n")    # ヘッダ情報出力
print("\r\n")                                                   # 空行出力

string = ENV["QUERY_STRING"]

string = string.split("&")
ary = []
string.each{ |object|
  ary.push(object.split("="))
}
hash = Hash[ary]

ary = []
hash.each { |key,value|
  ary.push(key)
  if(value != nil) then
    ary.push(value.gsub("+"," "))
  else
    ary.push("")
  end
}

hash = Hash[*ary]

ary = []
hash.each { |key,value|
  ary.push(key)
  if(value != nil) then
    ary.push(value.gsub(/((?:%[0-9a-fA-F][0-9a-fA-F])+)/n) do
               [$1.delete('%')].pack('H*') end)
  else
    ary.push("")
  end
}

hash = Hash[*ary]
hash.each{ |key,value|
  print("\n")
  print(" #{key}: #{value}")
  print("\n")
  print("-------------------------------------------Result-------------------------------------------\n")

  db = SQLite3::Database.new("tweet.db")
  if "#{value}" != "" 
    db.transaction{
      db.execute("select * from timeline where #{key} like '%#{value}%';") {|row|
        puts row.join("|")
      }
    }
  end
  db.close  
}
