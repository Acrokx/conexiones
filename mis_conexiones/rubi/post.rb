require 'pg'

conn = PG.connect(dbname: 'tienda', user: 'acroxmen', password: '12345', host: 'localhost')
res = conn.exec('SELECT * FROM tabla')

res.each do |row|
  puts row
end

conn.close
