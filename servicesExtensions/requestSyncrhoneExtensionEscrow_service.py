from typing import Any, List
from web3 import Web3 as WEB3

from artifacts import *
from config import config
from servicesCore.requestCore_service import RequestCoreService
from servicesExternal.web3_single import Web3Single

requestCoreArtifact = Artifacts.requestCoreArtifact
requestSynchroneExtensionEscrowArtifact = Artifacts.requestSynchroneExtensionEscrowArtifact
class RequestSynchroneExtensionEscrowService:
    def __init__(self):
        global requestCoreArtifact, requestSynchroneExtensionEscrowArtifact
        self._web3Single = Web3Single.getInstance()
        self._abiRequestCore = requestCoreArtifact.abi
        self._requestCoreServices = RequestCoreService()
        networkName = self._web3Single.networkName
        self._abiSynchroneExtensionEscrow = requestSynchroneExtensionEscrowArtifact.abi
        if not requestSynchroneExtensionEscrowArtifact[networkName] :
            raise ValueError('Escrow Artifact no configuration for network: ' + networkName)
        self._addressSynchroneExtensionEscrow = requestSynchroneExtensionEscrowArtifact.networks[networkName].address
        self._instanceSynchroneExtensionEscrow = self._web3Single.web3.eth.Contract(
            self._abiSynchroneExtensionEscrow,
            self._addressSynchroneExtensionEscrow)

    def parseParameters(self, extensionParams: List[Any]) -> Any:
        if not extensionParams or not self._web3Single.isAddressNoChecksum(extensionParams[0]):
            return {'error' : ValueError('first parameter must be a valid eth address')}
        ret : List[Any] = []
        #no idea about address parameter
        ret.append(self._web3Single.toSolidityBytes32(address, extensionParams[0]))
        for i in range(1,9):
            ret.append(self._web3Single.toSolidityBytes32('bytes32',0))
        return {'result' : ret}


    def releaseToPayeeAction(self, requestId: str, options: Any = None):
        pass

    def getRequest(self, requestId: str):
        pass

    def getRequestExtensionInfo(self, requestId: str):
        pass

    def getRequestEvents(self, requestId: str, fromBlock: int = None, toBlock: int = None):
        pass

    def getRequestEventsExtensionInfo(self, requestId: str, fromBlock: int = None, toBlock: int = None):
        pass

