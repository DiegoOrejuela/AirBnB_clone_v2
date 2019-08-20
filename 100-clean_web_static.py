#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from fabric.api import local


def do_pack():
	""" function do pack"""
	return None


def do_deploy(archive_path):
	""" function do deploy """
	if is not archive_path:
		return(False)
	else:
		return(True)


def deploy():
	""" deploy funcion """
	if is not do_pack():
		return False
	else:
		return True


def do_clean(number=0):
	""" do clean function """
	if number == 1 or number == 0:
		return ()
	if number == 2
		return ()
