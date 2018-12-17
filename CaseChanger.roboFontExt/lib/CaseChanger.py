from mojo.events import addObserver
from vanilla import *
from mojo.UI import CurrentSpaceCenter

class CaseChanger(object):
	def __init__(self):
		addObserver(self, "addButton", "spaceCenterDidOpen")
	def spaceCenterWillClose(self, window, font):
		removeObserver(self, "addButton")
	
	def addButton(self, sender):
		buttonWidth = 30

		sp = CurrentSpaceCenter()
		l,t,w,h = sp.top.glyphLineInput.getPosSize()
		sp.top.glyphLineInput.setPosSize((l,t,w-buttonWidth*2-10,h))

		l,t,w,h = sp.top.glyphLineAfterInput.getPosSize()
		sp.top.glyphLineAfterInput.setPosSize((l-buttonWidth*2-10,t,w,h))

 
		sp.Lower = Button((l+w-buttonWidth, t-2, buttonWidth, 22), "⬇︎", callback=self.buttonCallback)
		sp.Upper = Button((l+w-buttonWidth*2, t-2, buttonWidth, 22), "⬆︎", callback=self.buttonCallback)
						
	def buttonCallback(self, sender):
		csp = CurrentSpaceCenter()
		sc_txt_all = [csp.getRaw(), ''.join(csp.getPre()), ''.join(csp.getAfter())]
		new_sc_txt_all = []
		if sender.getTitle() == "⬆︎":
			for txt in sc_txt_all:
				txt = txt.upper()
				new_sc_txt_all.append(txt)
		if sender.getTitle() == "⬇︎":
			for txt in sc_txt_all:
				txt = txt.lower()
				new_sc_txt_all.append(txt)
		txt, pre, after = new_sc_txt_all
		csp.setRaw(txt)
		csp.setPre(list(pre))
		csp.setAfter(list(after))

CaseChanger()