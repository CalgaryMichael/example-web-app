-- This is (perhaps obviously) for local purposes only.
-- For running in prod, ensure that you replace the password
-- value for a reasonably complex value. Capture this password
-- and store it in a secure location (e.g. Secrets Manager service)
CREATE USER example_user WITH PASSWORD 'example';
