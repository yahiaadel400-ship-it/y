class DigitalClock {
    constructor() {
        this.selectedTimezones = ['UTC'];
        this.format24 = true;
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.populateTimezoneSelect();
        this.renderClocks();
        this.startClock();
    }

    setupEventListeners() {
        document.getElementById('addBtn').addEventListener('click', () => this.addTimezone());
        document.getElementById('timezoneSelect').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.addTimezone();
        });
        document.getElementById('format24').addEventListener('change', (e) => {
            this.format24 = e.target.checked;
        });
    }

    populateTimezoneSelect() {
        const select = document.getElementById('timezoneSelect');
        TIMEZONES.forEach(tz => {
            const option = document.createElement('option');
            option.value = tz.name;
            option.textContent = `${tz.city} (UTC${this.formatOffset(tz.offset)})`;
            select.appendChild(option);
        });
    }

    formatOffset(offset) {
        if (offset === 0) return '±0:00';
        const sign = offset > 0 ? '+' : '';
        const hours = Math.floor(Math.abs(offset));
        const minutes = (Math.abs(offset) % 1) * 60;
        return `${sign}${hours}:${minutes.toString().padStart(2, '0')}`;
    }

    addTimezone() {
        const select = document.getElementById('timezoneSelect');
        const timezone = select.value;

        if (!timezone) {
            alert('Please select a timezone');
            return;
        }

        if (this.selectedTimezones.includes(timezone)) {
            alert('This timezone is already added');
            return;
        }

        this.selectedTimezones.push(timezone);
        select.value = '';
        this.renderClocks();
    }

    removeTimezone(timezone) {
        this.selectedTimezones = this.selectedTimezones.filter(tz => tz !== timezone);
        this.renderClocks();
    }

    getTimeForTimezone(timezone) {
        // Get current UTC time
        const now = new Date();
        const utcString = now.toLocaleString('en-US', { timeZone: 'UTC' });
        const utcDate = new Date(utcString);

        // Get time in specified timezone
        const tzString = now.toLocaleString('en-US', { timeZone: timezone });
        const tzDate = new Date(tzString);

        return tzDate;
    }

    formatTime(date, format24) {
        const hours = String(date.getHours()).padStart(2, '0');
        const minutes = String(date.getMinutes()).padStart(2, '0');
        const seconds = String(date.getSeconds()).padStart(2, '0');

        if (format24) {
            return `${hours}:${minutes}:${seconds}`;
        } else {
            const hour12 = date.getHours() % 12 || 12;
            const period = date.getHours() >= 12 ? 'PM' : 'AM';
            return {
                time: `${String(hour12).padStart(2, '0')}:${minutes}:${seconds}`,
                period: period
            };
        }
    }

    formatDate(date) {
        const options = { weekday: 'short', month: 'short', day: 'numeric', year: 'numeric' };
        return date.toLocaleDateString('en-US', options);
    }

    renderClocks() {
        const container = document.getElementById('clocksContainer');
        container.innerHTML = '';

        if (this.selectedTimezones.length === 0) {
            container.innerHTML = `
                <div class="empty-state" style="grid-column: 1/-1;">
                    <h2>No timezones selected</h2>
                    <p>Add a timezone from the dropdown above to get started!</p>
                </div>
            `;
            return;
        }

        this.selectedTimezones.forEach(timezone => {
            const tzData = TIMEZONES.find(tz => tz.name === timezone);
            const date = this.getTimeForTimezone(timezone);
            const timeFormatted = this.formatTime(date, this.format24);
            const dateFormatted = this.formatDate(date);

            const clockCard = document.createElement('div');
            clockCard.className = 'clock-card';
            clockCard.innerHTML = `
                <button class="delete-btn" onclick="clock.removeTimezone('${timezone}')">×</button>
                <div class="timezone-name">${tzData.city.split(',')[0]}</div>
                <div class="timezone-label">${timezone}</div>
                <div class="analog-clock" data-timezone="${timezone}">
                    ${this.getAnalogClockHTML()}
                </div>
                <div class="digital-time">
                    ${this.format24 ? timeFormatted : timeFormatted.time}
                    ${!this.format24 ? `<div class="time-period">${timeFormatted.period}</div>` : ''}
                </div>
                <div class="date-info">${dateFormatted}</div>
            `;
            container.appendChild(clockCard);
        });
    }

    getAnalogClockHTML() {
        let html = '';
        for (let i = 1; i <= 12; i++) {
            const angle = (i * 30) - 90;
            html += `<div class="clock-number" style="transform: rotate(${angle}deg);"><span style="transform: rotate(${-angle}deg)">${i}</span></div>`;
        }
        html += '<div class="clock-center"></div>';
        html += '<div class="hand hour-hand"></div>';
        html += '<div class="hand minute-hand"></div>';
        html += '<div class="hand second-hand"></div>';
        return html;
    }

    updateClocks() {
        document.querySelectorAll('.clock-card').forEach(card => {
            const timezone = card.querySelector('.analog-clock').dataset.timezone;
            const date = this.getTimeForTimezone(timezone);
            const timeFormatted = this.formatTime(date, this.format24);

            // Update digital time
            const digitalTimeEl = card.querySelector('.digital-time');
            if (this.format24) {
                digitalTimeEl.textContent = timeFormatted;
            } else {
                digitalTimeEl.innerHTML = `${timeFormatted.time}<div class="time-period">${timeFormatted.period}</div>`;
            }

            // Update analog clock
            const hours = date.getHours() % 12;
            const minutes = date.getMinutes();
            const seconds = date.getSeconds();

            const hourHand = card.querySelector('.hour-hand');
            const minuteHand = card.querySelector('.minute-hand');
            const secondHand = card.querySelector('.second-hand');

            const hourDeg = (hours * 30) + (minutes * 0.5);
            const minuteDeg = (minutes * 6) + (seconds * 0.1);
            const secondDeg = seconds * 6;

            hourHand.style.transform = `rotate(${hourDeg}deg)`;
            minuteHand.style.transform = `rotate(${minuteDeg}deg)`;
            secondHand.style.transform = `rotate(${secondDeg}deg)`;
        });
    }

    startClock() {
        this.updateClocks();
        setInterval(() => this.updateClocks(), 1000);
    }
}

// Initialize the clock when DOM is ready
let clock;
document.addEventListener('DOMContentLoaded', () => {
    clock = new DigitalClock();
});
