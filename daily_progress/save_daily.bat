@echo off
color 0A
cls
echo ================================================
echo          Automatizacao de Commits GitHub
echo ================================================
echo.
echo Verificando alteracoes...
echo.

git status

echo.
echo ================================================
echo.
set /p msg="Digite o que voce fez hoje: "
echo.
echo Salvando alteracoes...
git add .
echo.
echo Criando commit...
git commit -m "docs: %msg%"
echo.
echo Enviando para GitHub...
git push
echo.
echo ================================================
echo                 TUDO PRONTO!
echo    Suas alteracoes foram salvas com sucesso!
echo    Verifique o quadrinho verde no GitHub :)
echo ================================================
echo.
pause