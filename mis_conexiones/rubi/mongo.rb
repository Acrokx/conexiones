require 'mongo'

client = Mongo::Client.new(['127.0.0.1:27017'], database: 'mi_clase')
collection = client[:usuario]

collection.find.each { |doc| puts doc }
