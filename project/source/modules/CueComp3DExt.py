CueComp = op.FPlayer.op('modules/CueComp').module.CueComp
ParProps = op.FPlayer.op('modules/ParProperties').module
mathFunc = op.FPlayer.op('modules/kMath').module
listFunc = op.FPlayer.op('modules/listFunc').module

class CueComp2DExt(CueComp):
	"""
	default custom content component for rendering 3D content
	across nodes.
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		CueComp.__init__(self, ownerComp)
		ParProps.parProperties(self, parCallbacksDAT=ownerComp.op('parCallbacks'))
		self.cam = self.ownerComp.op('cam')
		self.projMatDat = self.cam.op('projMatrix')
		self.render = self.ownerComp.op('render')


	def SetupCamRender(self):

		if self.NODE.Ispreviewrender:
			resX = self.NODE.Noderendersizew
			resY = self.NODE.Noderendersizeh
			cropLeft = 0.0
			cropRight = resX
			cropBottom = 0.0
			cropTop = resY

		else:
			resX = self.NODE.Canvassizew
			resY = self.NODE.Canvassizeh
			cropLeft = self.NODE.Noderenderoffsetx
			cropRight = cropLeft + self.NODE.Noderendersizew
			cropBottom = self.NODE.Noderenderoffsety
			cropTop = cropBottom + self.NODE.Noderendersizeh

		if self.Projection == 'PERSPECTIVE':

			camRenderData = mathFunc.MatMath.CalcProjM(	
				self.Fov, resX, resY, self.Near, self.Far, 
				cropLeft, cropRight, cropBottom, cropTop)

				
		else:
			camRenderData = mathFunc.MatMath.CalcOrthoProjM(	
				self.Orthowidth, resX, resY, self.Near, self.Far, 
				cropLeft, cropRight, cropBottom, cropTop)

		
		
		listFunc.MListFillTable(camRenderData[1], self.projMatDat)	
		self.render.par.resolution1 = camRenderData[2]
		self.render.par.resolution2 = camRenderData[3]	

		pass
		