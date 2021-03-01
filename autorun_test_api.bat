@echo off
ECHO ####################################################################################################
ECHO # Bienvenue dans ce script qui lancera les tests de vos fonctions et de votre API automatiquement. #
ECHO ####################################################################################################
set/p choix=Read-host -Prompt 'Souhaitez-vous effectuer les tests ? Y/N :'
if /i "%choix%" == "Y" (
ECHO ########################################
ECHO # Lancement des test de vos fonctions. #
ECHO ########################################
python test_fonction.py -v
ECHO ############################################################
ECHO # Les tests de vos fonctions se sont effectues avec succes #
ECHO ############################################################
ECHO ######################################
ECHO #  Lancement des test de votre API.  #
ECHO ######################################
python api_test.py -v
ECHO ############################################################
ECHO # Les tests de vos fonctions se sont effectues avec succes #
ECHO ############################################################
ECHO ############################################################
ECHO #            Votre API est prete a l'emploi                #
ECHO ############################################################
pause
)
set/p apirun=Read-host -Prompt 'Souhaitez-vous lancer votre API ? Y/N :'
if /i "%apirun%" == "Y" (
ECHO ########################################
ECHO #         Lancement de l'API.          #
ECHO ########################################
python api.py
)
