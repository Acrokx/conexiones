const { Client } = require('pg');

const client = new Client({
  user: 'postgres',
  host: 'postgres',
  database: 'tienda',
  password: '12345',
  port: 5432,
});

client.connect();

client.query('SELECT * FROM tabla', (err, res) => {
  if (err) {
    console.error(err);
  } else {
    console.log(res.rows);
  }
  client.end();
});
