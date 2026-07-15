#!/usr/bin/env python3
"""Connexion manuelle unique au compte Facebook (profil navigateur dédié).

Ouvre une fenêtre Chrome sur facebook.com : connectez-vous au compte dummy,
le script détecte la connexion, enregistre la session dans .fb-profile/ et
ferme tout. À relancer seulement si la session expire.
"""
import os
import sys
import time

from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(BASE, ".fb-profile")

def logged_in(ctx):
    return any(c["name"] == "c_user" for c in ctx.cookies("https://www.facebook.com"))

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        PROFILE, headless=False, locale="fr-CA",
        viewport={"width": 1240, "height": 900},
        args=["--disable-blink-features=AutomationControlled"],
    )
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    if logged_in(ctx):
        print("Déjà connecté — rien à faire.")
        ctx.close()
        sys.exit(0)
    page.goto("https://www.facebook.com/login")
    print("Fenêtre ouverte : connectez-vous au compte dummy (10 minutes max)...")
    for _ in range(300):
        time.sleep(2)
        try:
            if logged_in(ctx):
                print("Connexion détectée. Session enregistrée dans .fb-profile/")
                time.sleep(3)
                ctx.close()
                sys.exit(0)
        except Exception:
            break
    print("Pas de connexion détectée (fenêtre fermée ou délai dépassé).")
    try:
        ctx.close()
    except Exception:
        pass
    sys.exit(1)
