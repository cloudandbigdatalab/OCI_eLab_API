import cloudModules.cloudAuth as cloudAuth
import cloudModules.cloudCompute as cloudCompute
import cloudModules.cloudImages as cloudImages
import configuration.globalVars as globalVars
import apiModules.update as update
import apiModules.registerUser as register


globalVars.init()  #Initialize global variables

my_token_id = cloudAuth.auth()

#cloudCompute.bootVM(my_token_id, 'server_testing1', 'eec1fa2e-a8ba-4725-ab6c-2c65acb958fc')
#cloudImages.getImageList(my_token_id)
#cloudCompute.queryVM(my_token_id, '73fa6abc-a844-41c1-85eb-948b4af3240f')
#update.updateCatalog(my_token_id)

register.registerUser('PaulRad', my_token_id)
