// const http = require('http');

// // Define the hostname and port
// const hostname = '127.0.0.1';
// const port = 3232;

// // Create the HTTP server
// const server = http.createServer((req, res) => {
//   // Set the response header with HTTP status and content type
//   res.statusCode = 200;
//   res.setHeader('Content-Type', 'text/plain');

//   // Send the response body
//   res.end('Helklo, World!\n');
// });

// // Start the server and listen on the defined hostname and port
// server.listen(port, hostname, () => {
//   console.log(`Server running at http://${hostname}:${port}/`);
// });





const http = require('http');

// In-memory array to act as our "database"
let items = [];

// Define the hostname and port
const hostname = '127.0.0.1';
const port = 3000;

// Helper function to parse JSON body data
const parseBody = (req) => {
  return new Promise((resolve, reject) => {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
    });
    req.on('end', () => {
      resolve(JSON.parse(body));
    });
  });
};

// Create the HTTP server
const server = http.createServer(async (req, res) => {
  const { method, url } = req;

  // Handle GET request: Read all items
  if (method === 'GET' && url === '/items') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(items));

  // Handle POST request: Create a new item
  } else if (method === 'POST' && url === '/items') {
    const newItem = await parseBody(req);
    items.push(newItem);
    res.statusCode = 201;
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(newItem));

  // Handle PUT request: Update an existing item
  } else if (method === 'PUT' && url.startsWith('/items/')) {
    const id = parseInt(url.split('/')[2]);
    const updatedItem = await parseBody(req);

    if (id >= 0 && id < items.length) {
      items[id] = updatedItem;
      res.statusCode = 200;
      res.setHeader('Content-Type', 'application/json');
      res.end(JSON.stringify(updatedItem));
    } else {
      res.statusCode = 404;
      res.setHeader('Content-Type', 'application/json');
      res.end(JSON.stringify({ error: 'Item not found' }));
    }

  // Handle DELETE request: Delete an item
  } else if (method === 'DELETE' && url.startsWith('/items/')) {
    const id = parseInt(url.split('/')[2]);

    if (id >= 0 && id < items.length) {
      items.splice(id, 1);
      res.statusCode = 204;
      res.end();
    } else {
      res.statusCode = 404;
      res.setHeader('Content-Type', 'application/json');
      res.end(JSON.stringify({ error: 'Item not found' }));
    }

  // Handle invalid routes
  } else {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify({ error: 'Route not found' }));
  }
});

// Start the server and listen on the defined hostname and port
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
