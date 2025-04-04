const mysql = require('mysql');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '12345',
  database: 'tienda'
});

connection.connect();

connection.query('SELECT * FROM tabla', (error, results) => {
  if (error) throw error;
  console.log(results);
});

connection.end();
