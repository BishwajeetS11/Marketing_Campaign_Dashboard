-- Create campaigns table
CREATE TABLE IF NOT EXISTS campaigns (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL CHECK (status IN ('Active', 'Paused')),
    clicks INTEGER NOT NULL DEFAULT 0 CHECK (clicks >= 0),
    cost DECIMAL(10, 2) NOT NULL DEFAULT 0.00 CHECK (cost >= 0),
    impressions INTEGER NOT NULL DEFAULT 0 CHECK (impressions >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_campaigns_status ON campaigns(status);
CREATE INDEX IF NOT EXISTS idx_campaigns_name ON campaigns(name);

-- Insert sample data
INSERT INTO campaigns (name, status, clicks, cost, impressions) VALUES
('Summer Sale', 'Active', 150, 45.99, 1000),
('Black Friday', 'Paused', 320, 89.50, 2500),
('Holiday Special', 'Active', 275, 120.75, 3200),
('Spring Launch', 'Active', 198, 67.30, 1850),
('Back to School', 'Paused', 410, 155.20, 4100),
('Winter Clearance', 'Active', 89, 32.15, 950),
('New Year Promo', 'Active', 502, 210.80, 5500),
('Valentine''s Day', 'Paused', 145, 58.90, 1600),
('Easter Campaign', 'Active', 223, 95.40, 2800),
('Cyber Monday', 'Paused', 678, 299.99, 7200);