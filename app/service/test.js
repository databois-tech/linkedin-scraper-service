
const cookies = [
    {
        name: 'li_rm', 
        value: 'AQEnWrhgFJGQfQAAAZH-cGhzcroqBXwayymPyNtIGEZQo93W7r1HIJB8O55xlvdjAVtcF87ANBYz-aFs5N2yv5BrRFnkIH8fQpGfJNau_-J5Sz4oM0DzuXwD', 
        domain: '.www.linkedin.com', 
        path: '/', 
        expires: 1758086669.867428, 
        httpOnly: true, 
        secure: true, 
        sameSite: 'None'
    },
    {
        name: 'lang', 
        value: 'v=2&lang=en-us', 
        domain: '.linkedin.com', 
        path: '/', 
        expires: -1, 
        httpOnly: false, 
        secure: true, 
        sameSite: 'None'
    },
    {
        name: 'JSESSIONID', 
        value: 'ajax:5969587573258662047', 
        domain: '.www.linkedin.com', 
        path: '/', 
        expires: 1734326669.867881, 
        httpOnly: false, 
        secure: true, 
        sameSite: 'None'
    },
    {
        name: 'bcookie', 
        value: 'v=2&4b9dc2b7-9d05-436c-8fe1-2ff37ba8ab5e', 
        domain: '.linkedin.com', 
        path: '/', 
        expires: 1758086670.867945, 
        httpOnly: false, 
        secure: true, 
        sameSite: 'None'
    },
    {
        name: 'bscookie', 
        value: 'v=1&2024091705242564bf525a-aaac-4135-8498-3ab0076f5197AQHvcJSh7t_KIVcs9jProcwKeOqdZUsJ', 
        domain: '.www.linkedin.com', 
        path: '/', 
        expires: 1758086670.868025, 
        httpOnly: true, 
        secure: true, 
        sameSite: 'None'
    },
    {
        name: 'liap', 
        value: 'true', 
        domain: '.linkedin.com', 
        path: '/', 
        expires: 1734326669.867755, 
        httpOnly: false, 
        secure: true, 
        sameSite: 'None'
    },
    {
        name: 'li_at', 
        value: 'AQEDAVJmCCcD-euYAAABkf5weS4AAAGSInz9Lk4Ax_upx2ahVF7ovM_BxPRYndwnsZlHswTRQ3V_6E8AQRXlSVOuZoIBm7iDqDJG410F1SdTB0FUMawe70bDSkktT8nKnBLh1AYtRxQN2Ks9E_64tcvb', 
        domain: '.www.linkedin.com', 
        path: '/', 
        expires: 1758086669.867827, 
        httpOnly: true, 
        secure: true, 
        sameSite: 'None'
    },
    {
        name: 'lidc', 
        value: 'b=VB71:s=V:r=V:a=V:p=V:g=3640:u=4:x=1:i=1726550670:t=1726635911:v=2:sig=AQFyvZ3cFvixE3JxN1mVz-Lk6uaXpvVG', 
        domain: '.linkedin.com', 
        path: '/', 
        expires: 1726635912.379133, 
        httpOnly: false, 
        secure: true, 
        sameSite: 'None'
    }
];

let chrome_cookie_value = "";
let csrf_val = "";
for (let cookie of cookies) {
    chrome_cookie_value += `${cookie.name}=${cookie.value}; `;

    if (cookie.name === "JSESSIONID") {
    csrf_val = cookie.value;
    }
}

const encodedCookie = encodeURIComponent(chrome_cookie_value);
console.log(encodedCookie);
