const electron = require('electron');
const path = require('path');
const url = require('url');
const MainWindow = require('./view/windows/main_window');

process.env.NODE_ENV = "development"; //TODO: Change at the time of production

const { app: sterling, ipcMain } = electron;

const developer = true;

let sterlingMainWindow;

function init_sterling() {

	sterlingMainWindow = new MainWindow(developer);

	sterlingMainWindow.createMainMenu();

	sterlingMainWindow.loadURL(url.format({
		pathname: path.join(__dirname, 'view/home.html'),
		protocol: 'file:',
		slashes: true
	}));
}

sterling.on('ready', init_sterling);

sterling.on('window-all-closed', () => {
	sterling.quit();
});