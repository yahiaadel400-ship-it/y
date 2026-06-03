// List of all available timezones
const TIMEZONES = [
    // UTC
    { name: 'UTC', offset: 0, city: 'Coordinated Universal Time' },

    // Americas
    { name: 'America/New_York', offset: -5, city: 'New York, USA' },
    { name: 'America/Chicago', offset: -6, city: 'Chicago, USA' },
    { name: 'America/Denver', offset: -7, city: 'Denver, USA' },
    { name: 'America/Los_Angeles', offset: -8, city: 'Los Angeles, USA' },
    { name: 'America/Anchorage', offset: -9, city: 'Anchorage, USA' },
    { name: 'Pacific/Honolulu', offset: -10, city: 'Honolulu, USA' },
    { name: 'America/Toronto', offset: -5, city: 'Toronto, Canada' },
    { name: 'America/Vancouver', offset: -8, city: 'Vancouver, Canada' },
    { name: 'America/Mexico_City', offset: -6, city: 'Mexico City, Mexico' },
    { name: 'America/Sao_Paulo', offset: -3, city: 'São Paulo, Brazil' },
    { name: 'America/Buenos_Aires', offset: -3, city: 'Buenos Aires, Argentina' },

    // Europe
    { name: 'Europe/London', offset: 0, city: 'London, UK' },
    { name: 'Europe/Paris', offset: 1, city: 'Paris, France' },
    { name: 'Europe/Berlin', offset: 1, city: 'Berlin, Germany' },
    { name: 'Europe/Madrid', offset: 1, city: 'Madrid, Spain' },
    { name: 'Europe/Rome', offset: 1, city: 'Rome, Italy' },
    { name: 'Europe/Amsterdam', offset: 1, city: 'Amsterdam, Netherlands' },
    { name: 'Europe/Moscow', offset: 3, city: 'Moscow, Russia' },
    { name: 'Europe/Istanbul', offset: 3, city: 'Istanbul, Turkey' },
    { name: 'Europe/Athens', offset: 2, city: 'Athens, Greece' },
    { name: 'Europe/Dublin', offset: 0, city: 'Dublin, Ireland' },
    { name: 'Europe/Stockholm', offset: 1, city: 'Stockholm, Sweden' },

    // Middle East & Africa
    { name: 'Asia/Dubai', offset: 4, city: 'Dubai, UAE' },
    { name: 'Asia/Baghdad', offset: 3, city: 'Baghdad, Iraq' },
    { name: 'Africa/Cairo', offset: 2, city: 'Cairo, Egypt' },
    { name: 'Africa/Johannesburg', offset: 2, city: 'Johannesburg, South Africa' },
    { name: 'Africa/Lagos', offset: 1, city: 'Lagos, Nigeria' },
    { name: 'Africa/Nairobi', offset: 3, city: 'Nairobi, Kenya' },

    // South Asia
    { name: 'Asia/Kolkata', offset: 5.5, city: 'New Delhi, India' },
    { name: 'Asia/Karachi', offset: 5, city: 'Karachi, Pakistan' },
    { name: 'Asia/Dhaka', offset: 6, city: 'Dhaka, Bangladesh' },
    { name: 'Asia/Bangkok', offset: 7, city: 'Bangkok, Thailand' },

    // East Asia
    { name: 'Asia/Shanghai', offset: 8, city: 'Shanghai, China' },
    { name: 'Asia/Hong_Kong', offset: 8, city: 'Hong Kong' },
    { name: 'Asia/Singapore', offset: 8, city: 'Singapore' },
    { name: 'Asia/Tokyo', offset: 9, city: 'Tokyo, Japan' },
    { name: 'Asia/Seoul', offset: 9, city: 'Seoul, South Korea' },
    { name: 'Asia/Manila', offset: 8, city: 'Manila, Philippines' },

    // Oceania
    { name: 'Australia/Sydney', offset: 11, city: 'Sydney, Australia' },
    { name: 'Australia/Melbourne', offset: 11, city: 'Melbourne, Australia' },
    { name: 'Australia/Brisbane', offset: 10, city: 'Brisbane, Australia' },
    { name: 'Australia/Perth', offset: 8, city: 'Perth, Australia' },
    { name: 'Pacific/Auckland', offset: 13, city: 'Auckland, New Zealand' },
    { name: 'Pacific/Fiji', offset: 12, city: 'Fiji' },
];

// Sort timezones by offset
TIMEZONES.sort((a, b) => a.offset - b.offset);

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = TIMEZONES;
}