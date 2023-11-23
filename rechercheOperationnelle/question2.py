'''
. Algo Branch&Bound( S=(F1;F0;L) , Best). {Maximisation}
2. Si (les contraintes sont respectées) alors
3. Score=eval(S)
4. Si (L=Ø ) alors
5. Si (Score > Best) alors
6. Best:=Score. // W
7. finsi
8. Sinon
9. Si (Score > Best) alors
10. x:=choisirVariable(L)
11. Branch&Bound( (F1U{x};F0;L\{x}) , Best)
12. Branch&Bound( (F1;F0U{x};L\{x}) , Best)
13. finsi
14. finsi
15. Finsi
16. Retourner Best
'''
