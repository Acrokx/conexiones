require 'mysql2'

client = Mysql2::Client.new(
  host: 'localhost',
  username: 'acroxmen',
  password: '12345',
  database: 'mi_clase'
)

results = client.query('SELECT * FROM tabla')
results.each do |row|
  puts row
end
