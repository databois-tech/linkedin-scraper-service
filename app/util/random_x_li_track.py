import random

# Array of X-Li-Track headers
x_li_tracks = [
    '{"clientVersion":"1.13.25033","mpVersion":"1.13.25033","osName":"web","timezoneOffset":5.5,"timezone":"Asia/Calcutta","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    '{"clientVersion":"1.13.26001","mpVersion":"1.13.26001","osName":"web","timezoneOffset":-7.0,"timezone":"America/Los_Angeles","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.25,"displayWidth":2560,"displayHeight":1440}',
    '{"clientVersion":"1.13.27015","mpVersion":"1.13.27015","osName":"web","timezoneOffset":0.0,"timezone":"Europe/London","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    '{"clientVersion":"1.13.24045","mpVersion":"1.13.24045","osName":"web","timezoneOffset":9.0,"timezone":"Asia/Tokyo","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":2,"displayWidth":1440,"displayHeight":900}',
    '{"clientVersion":"1.13.23012","mpVersion":"1.13.23012","osName":"web","timezoneOffset":1.0,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5,"displayWidth":1680,"displayHeight":1050}',
    '{"clientVersion":"1.13.25543","mpVersion":"1.13.25543","osName":"web","timezoneOffset":-3.0,"timezone":"America/Sao_Paulo","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.25,"displayWidth":1366,"displayHeight":768}',
    '{"clientVersion":"1.13.22008","mpVersion":"1.13.22008","osName":"web","timezoneOffset":2.0,"timezone":"Europe/Berlin","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1200}',
    '{"clientVersion":"1.13.28010","mpVersion":"1.13.28010","osName":"web","timezoneOffset":8.0,"timezone":"Asia/Hong_Kong","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":2,"displayWidth":2560,"displayHeight":1440}',
    '{"clientVersion":"1.13.26500","mpVersion":"1.13.26500","osName":"web","timezoneOffset":-5.0,"timezone":"America/New_York","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1600,"displayHeight":900}',
    '{"clientVersion":"1.13.27520","mpVersion":"1.13.27520","osName":"web","timezoneOffset":11.0,"timezone":"Pacific/Noumea","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5,"displayWidth":1360,"displayHeight":768}',
    '{"clientVersion":"1.13.22019","mpVersion":"1.13.22019","osName":"web","timezoneOffset":4.0,"timezone":"Asia/Dubai","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1366,"displayHeight":768}',
    '{"clientVersion":"1.13.22500","mpVersion":"1.13.22500","osName":"web","timezoneOffset":9.5,"timezone":"Australia/Adelaide","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.25,"displayWidth":2560,"displayHeight":1080}',
    '{"clientVersion":"1.13.23005","mpVersion":"1.13.23005","osName":"web","timezoneOffset":6.0,"timezone":"Asia/Almaty","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1280,"displayHeight":720}',
    '{"clientVersion":"1.13.24500","mpVersion":"1.13.24500","osName":"web","timezoneOffset":10.0,"timezone":"Pacific/Port_Moresby","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5,"displayWidth":1920,"displayHeight":1080}',
    '{"clientVersion":"1.13.21540","mpVersion":"1.13.21540","osName":"web","timezoneOffset":3.0,"timezone":"Europe/Moscow","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1600,"displayHeight":900}',
    '{"clientVersion":"1.13.29030","mpVersion":"1.13.29030","osName":"web","timezoneOffset":-8.0,"timezone":"America/Anchorage","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.25,"displayWidth":1440,"displayHeight":900}',
    '{"clientVersion":"1.13.21033","mpVersion":"1.13.21033","osName":"web","timezoneOffset":12.0,"timezone":"Pacific/Auckland","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":2,"displayWidth":2880,"displayHeight":1800}',
    '{"clientVersion":"1.13.26020","mpVersion":"1.13.26020","osName":"web","timezoneOffset":7.0,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.25,"displayWidth":1920,"displayHeight":1200}',
    '{"clientVersion":"1.13.23500","mpVersion":"1.13.23500","osName":"web","timezoneOffset":-4.0,"timezone":"America/Caracas","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    '{"clientVersion":"1.13.28500","mpVersion":"1.13.28500","osName":"web","timezoneOffset":2.0,"timezone":"Africa/Johannesburg","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.25,"displayWidth":1440,"displayHeight":900}'
]

# Function to pick a random X-Li-Track header
def get_random_x_li_track():
    return random.choice(x_li_tracks)