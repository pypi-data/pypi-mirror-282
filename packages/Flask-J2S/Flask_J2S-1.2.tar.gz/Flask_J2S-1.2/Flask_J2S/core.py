from Modul_Wrapper import Wrap
import inspect

class Processing(Wrap):
	def __init__(kimin, **parameter):
		kimin.parameter = parameter
		super().__init__(modul_path=parameter.get('path_modul', {"modul":[]}))
		kimin.base_dir = kimin.Base_Dir()
	
	def Base_Dir(kimin):
		path = inspect.stack()[1]
		path = path.filename
		return kimin.modul['os'].path.dirname(kimin.modul['os'].path.abspath(path))
	
	def Run_Server(kimin):
		x = kimin.modul['server'](config=kimin.parameter['config_path'], modul=kimin.modul, base_dir=kimin.base_dir)
		if len(kimin.modul['sys'].argv) > 1 and kimin.modul['sys'].argv[1] == 'generate':
			x.Prepare()
			print("File Routes Berhasil Di Generate\nSilahkan Jalankan Ulang!!")
			kimin.modul['sys'].exit(1)
		
		elif len(kimin.modul['sys'].argv) > 1 and kimin.modul['sys'].argv[1] == 'set-fe':
			x.Set_FE()
			print("File File Berhasil Di Generate\nSilahkan Jalankan Ulang!!")
			kimin.modul['sys'].exit(1)
		
		server = x.Server()
		kimin.modul['cors'](server)
		x.Routes(server)
		x.Run(server)