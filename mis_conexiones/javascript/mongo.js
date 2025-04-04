const { MongoClient } = require('mongodb');

async function conectar() {
  const client = new MongoClient('mongodb://localhost:27017');
  await client.connect();
  const db = client.db('tienda');
  const collection = db.collection('productos');

  const documentos = await collection.find().toArray();
  console.log(documentos);

  await client.close();
}

conectar();
