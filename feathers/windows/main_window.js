const electron = require('electron');

const { app: sterling, BrowserWindow, Menu } = electron;

class MainWindow extends BrowserWindow {

    constructor(developer) {
        super({
            width: 960,
            height: 700,
            minWidth: 780,
            minHeight: 500,
            kiosk: false,
            title: "Sterling", 
            frame: true, //TODO: change the frame display setting on production
            titleBarStyle: (process.platform == 'darwin') ? 'hiddenInset' : '',
            show: false,
            webPreferences: {
                devTools: developer,
                nodeIntegration: false,
                contextIsolation: true,
                safeDialogs: true,
                preload: 'preload.js'
            }
        })

        this.once('ready-to-show', () => { 
            this.show(); 
        });

	    this.on('closed', () => {
            sterling.quit();
        });
    }
        

    createMainMenu() {

        const sterlingMenuTemplate = [
            {
                label: 'Edit',
                submenu: [
                    { role: 'undo' },
                    { role: 'redo' },
                    { role: 'cut' },
                    { role: 'copy' },
                    { role: 'paste' }
                ]
            }
        ];

        if (process.platform === 'darwin') sterlingMenuTemplate.unshift({
            label: sterling.getName(),
            submenu: [
                { role: 'about' },
                { role: 'hide' },
                { role: 'unhide' },
                { role: 'quit' }
            ]
        });

        if (process.env.NODE_ENV !== 'production') sterlingMenuTemplate.push({
            label: 'Developer Tools',
            submenu: [
                { role: 'reload' },
                { role: 'toggledevtools' }
            ]
        });
    
        const mainMenu = Menu.buildFromTemplate(sterlingMenuTemplate);
    
        Menu.setApplicationMenu(mainMenu);
    }

}

module.exports = MainWindow;