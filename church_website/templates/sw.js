const CACHE_NAME = 'scripture-champions-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/static/img/logo.png',
  'https://cdn.tailwindcss.com',
  'https://cdn.jsdelivr.net/npm/remixicon@4.5.0/fonts/remixicon.css'
];

// Install Event
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
});

// Activate Event
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      );
    })
  );
});

// Fetch Event
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      // Return cached response if found, otherwise fetch from network
      return cachedResponse || fetch(event.request).then((response) => {
        // Optional: Cache new requests on the fly
        return response;
      });
    })
  );
});
