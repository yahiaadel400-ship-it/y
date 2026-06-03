# 🕐 Digital Clock with Multiple Time Zones

A beautiful, interactive digital clock application that displays the current time in different time zones around the world.

## Features ✨

- **Multiple Time Zones**: Display time in 45+ different time zones
- **Dual Display**: Both digital and analog clock representations
- **24/12 Hour Format**: Toggle between 24-hour and 12-hour (AM/PM) format
- **Real-time Updates**: Clock updates every second with smooth animations
- **Easy Management**: Add and remove time zones with a single click
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Beautiful UI**: Modern gradient design with smooth transitions and hover effects
- **Date Display**: Shows the date in each timezone
- **No Dependencies**: Pure vanilla JavaScript, HTML, and CSS

## Supported Time Zones 🌍

### Americas
- New York, Chicago, Denver, Los Angeles
- Anchorage, Honolulu
- Toronto, Vancouver
- Mexico City
- São Paulo, Buenos Aires

### Europe
- London, Paris, Berlin, Madrid
- Rome, Amsterdam, Stockholm
- Moscow, Istanbul, Athens, Dublin

### Middle East & Africa
- Dubai, Baghdad
- Cairo, Johannesburg
- Lagos, Nairobi

### South Asia
- New Delhi (India)
- Karachi (Pakistan)
- Dhaka (Bangladesh)
- Bangkok (Thailand)

### East Asia
- Shanghai, Hong Kong
- Singapore, Tokyo
- Seoul, Manila

### Oceania
- Sydney, Melbourne, Brisbane
- Perth, Auckland, Fiji

## Getting Started 🚀

### Simple Usage

1. Open `index.html` in your web browser
2. Select a timezone from the dropdown menu
3. Click "+ Add Timezone" or press Enter
4. See the clock update in real-time
5. Toggle the "24-Hour Format" checkbox to switch between 24-hour and 12-hour display

### File Structure

```
digital-clock/
├── index.html       # Main HTML file
├── styles.css       # Complete styling
├── clock.js         # Clock logic and functionality
├── timezones.js     # List of all available timezones
└── README.md        # This file
```

## How It Works 🔧

### Clock Class

The `DigitalClock` class manages:
- Timezone selection and management
- Time formatting (24-hour and 12-hour)
- Analog and digital clock rendering
- Real-time updates

### Key Methods

- `addTimezone()` - Add a new timezone to the display
- `removeTimezone(timezone)` - Remove a timezone from the display
- `getTimeForTimezone(timezone)` - Get the current time for a specific timezone
- `formatTime(date, format24)` - Format time based on the selected format
- `updateClocks()` - Update all clock displays (called every second)
- `renderClocks()` - Re-render the clock cards

### Time Calculation

The application uses JavaScript's `toLocaleString()` method with timezone parameter to accurately calculate local time in different zones:

```javascript
const now = new Date();
const tzString = now.toLocaleString('en-US', { timeZone: timezone });
const tzDate = new Date(tzString);
```

## Customization 🎨

### Add Custom Colors

Edit the gradient colors in `styles.css`:

```css
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### Modify Clock Appearance

Adjust the clock card styling:

```css
.clock-card {
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}
```

### Add New Timezones

Edit `timezones.js` and add to the `TIMEZONES` array:

```javascript
{
    name: 'Asia/Bangkok',
    offset: 7,
    city: 'Bangkok, Thailand'
}
```

## Browser Compatibility 🌐

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## Features Breakdown 📊

### Digital Time Display
- Large, easy-to-read numbers
- Monospace font for clarity
- AM/PM indicator (in 12-hour mode)
- Smooth updates every second

### Analog Clock
- Hour, minute, and second hands
- Color-coded hands (different colors for visual clarity)
- Smooth rotation animations
- Numbered clock face (1-12)

### Timezone Management
- Dropdown selection from 45+ timezones
- Prevents duplicate timezone additions
- One-click deletion with hover effect
- Shows current UTC offset for each timezone

### Responsive Design
- Grid layout that adapts to screen size
- Touch-friendly buttons on mobile
- Readable text at all sizes
- Smooth animations across devices

## Tips & Tricks 💡

1. **Quick Timezone Switch**: Click the "×" button (visible on hover) to quickly remove a timezone
2. **Timezone Search**: Start typing in the dropdown to filter timezones
3. **Multiple Instances**: Open multiple browser windows for different timezone sets
4. **Format Toggle**: Use the checkbox to switch between 24-hour and 12-hour format on the fly

## Performance Optimization ⚡

- Minimal DOM manipulation
- Single interval for all clock updates
- CSS transitions for smooth animations
- No external dependencies

## Accessibility ♿

- Clear, readable fonts
- High contrast colors
- Keyboard navigation support
- Semantic HTML structure
- Clear labels and descriptions

## License 📄

This project is open source and available under the MIT License.

## Contributing 🤝

Feel free to fork, modify, and improve this clock application!

## Author 👨‍💻

Created with ❤️ for clock enthusiasts and timezone travelers!
