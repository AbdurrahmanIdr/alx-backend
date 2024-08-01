#!/usr/bin/node
/**
 * Connect to redis server via redis client
 */
import { createClient } from 'redis';

const client = createClient();



client.on('connect', () => {
  console.log('Redis client connected to the server');
});
