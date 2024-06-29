r'''
# `azuread_application_federated_identity_credential`

Refer to the Terraform Registry for docs: [`azuread_application_federated_identity_credential`](https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential).
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class ApplicationFederatedIdentityCredential(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.applicationFederatedIdentityCredential.ApplicationFederatedIdentityCredential",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential azuread_application_federated_identity_credential}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        audiences: typing.Sequence[builtins.str],
        display_name: builtins.str,
        issuer: builtins.str,
        subject: builtins.str,
        application_id: typing.Optional[builtins.str] = None,
        application_object_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ApplicationFederatedIdentityCredentialTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential azuread_application_federated_identity_credential} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param audiences: List of audiences that can appear in the external token. This specifies what should be accepted in the ``aud`` claim of incoming tokens. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#audiences ApplicationFederatedIdentityCredential#audiences}
        :param display_name: A unique display name for the federated identity credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#display_name ApplicationFederatedIdentityCredential#display_name}
        :param issuer: The URL of the external identity provider, which must match the issuer claim of the external token being exchanged. The combination of the values of issuer and subject must be unique on the app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#issuer ApplicationFederatedIdentityCredential#issuer}
        :param subject: The identifier of the external software workload within the external identity provider. The combination of issuer and subject must be unique on the app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#subject ApplicationFederatedIdentityCredential#subject}
        :param application_id: The resource ID of the application for which this federated identity credential should be created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#application_id ApplicationFederatedIdentityCredential#application_id}
        :param application_object_id: The object ID of the application for which this federated identity credential should be created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#application_object_id ApplicationFederatedIdentityCredential#application_object_id}
        :param description: A description for the federated identity credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#description ApplicationFederatedIdentityCredential#description}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#id ApplicationFederatedIdentityCredential#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#timeouts ApplicationFederatedIdentityCredential#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25e7d867a9c90dd50d1c04323bf335c3ebc4b1f16da64e62094a4e1357724a72)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApplicationFederatedIdentityCredentialConfig(
            audiences=audiences,
            display_name=display_name,
            issuer=issuer,
            subject=subject,
            application_id=application_id,
            application_object_id=application_object_id,
            description=description,
            id=id,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a ApplicationFederatedIdentityCredential resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the ApplicationFederatedIdentityCredential to import.
        :param import_from_id: The id of the existing ApplicationFederatedIdentityCredential that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the ApplicationFederatedIdentityCredential to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__111b1a919c696bc3efee258450c5965254c3e70e0547684e1117880b953b089f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#create ApplicationFederatedIdentityCredential#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#delete ApplicationFederatedIdentityCredential#delete}.
        :param read: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#read ApplicationFederatedIdentityCredential#read}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#update ApplicationFederatedIdentityCredential#update}.
        '''
        value = ApplicationFederatedIdentityCredentialTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetApplicationId")
    def reset_application_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationId", []))

    @jsii.member(jsii_name="resetApplicationObjectId")
    def reset_application_object_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationObjectId", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="credentialId")
    def credential_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentialId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "ApplicationFederatedIdentityCredentialTimeoutsOutputReference":
        return typing.cast("ApplicationFederatedIdentityCredentialTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="applicationIdInput")
    def application_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationObjectIdInput")
    def application_object_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationObjectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="audiencesInput")
    def audiences_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "audiencesInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ApplicationFederatedIdentityCredentialTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ApplicationFederatedIdentityCredentialTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc1bbf78a3d6b6b79a10ff480fe2806af9d9302f1f60524758ae81f1a6c9e529)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="applicationObjectId")
    def application_object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationObjectId"))

    @application_object_id.setter
    def application_object_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfd1680fb38a49dafdede89fce7461301d9ddd1cdb08bc4828970fee0f01927e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationObjectId", value)

    @builtins.property
    @jsii.member(jsii_name="audiences")
    def audiences(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "audiences"))

    @audiences.setter
    def audiences(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7fb37025ae1dfd2127ce740fc31e7b87a02fddb657e0a1b12f2be5da85c63de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audiences", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cec3c9e74e1c495e2549c561369e2a01ff51cce2f53160f37f5b4ceb9a45a05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c18811a40e13ac2a450068f666e9a3f8589f90fcbe9f0762da8af397b3aa065)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ac30bffc1397fb5ecb505928adf40c5948a3c2a94154764b207801188bc4ce2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cf69a291e80b5188a723380593f321438c646649363cc41a16935d714eb4f40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @subject.setter
    def subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb4d7a5e18eeea9742686c92baaaa5a0717c636145e10208a5700c279ca730ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subject", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.applicationFederatedIdentityCredential.ApplicationFederatedIdentityCredentialConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "audiences": "audiences",
        "display_name": "displayName",
        "issuer": "issuer",
        "subject": "subject",
        "application_id": "applicationId",
        "application_object_id": "applicationObjectId",
        "description": "description",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class ApplicationFederatedIdentityCredentialConfig(
    _cdktf_9a9027ec.TerraformMetaArguments,
):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        audiences: typing.Sequence[builtins.str],
        display_name: builtins.str,
        issuer: builtins.str,
        subject: builtins.str,
        application_id: typing.Optional[builtins.str] = None,
        application_object_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ApplicationFederatedIdentityCredentialTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param audiences: List of audiences that can appear in the external token. This specifies what should be accepted in the ``aud`` claim of incoming tokens. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#audiences ApplicationFederatedIdentityCredential#audiences}
        :param display_name: A unique display name for the federated identity credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#display_name ApplicationFederatedIdentityCredential#display_name}
        :param issuer: The URL of the external identity provider, which must match the issuer claim of the external token being exchanged. The combination of the values of issuer and subject must be unique on the app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#issuer ApplicationFederatedIdentityCredential#issuer}
        :param subject: The identifier of the external software workload within the external identity provider. The combination of issuer and subject must be unique on the app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#subject ApplicationFederatedIdentityCredential#subject}
        :param application_id: The resource ID of the application for which this federated identity credential should be created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#application_id ApplicationFederatedIdentityCredential#application_id}
        :param application_object_id: The object ID of the application for which this federated identity credential should be created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#application_object_id ApplicationFederatedIdentityCredential#application_object_id}
        :param description: A description for the federated identity credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#description ApplicationFederatedIdentityCredential#description}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#id ApplicationFederatedIdentityCredential#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#timeouts ApplicationFederatedIdentityCredential#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ApplicationFederatedIdentityCredentialTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdfc444dacef508005ea0cec487aaa3d820cafcee1a9771fd65224d8369e8236)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument audiences", value=audiences, expected_type=type_hints["audiences"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument application_object_id", value=application_object_id, expected_type=type_hints["application_object_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "audiences": audiences,
            "display_name": display_name,
            "issuer": issuer,
            "subject": subject,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if application_id is not None:
            self._values["application_id"] = application_id
        if application_object_id is not None:
            self._values["application_object_id"] = application_object_id
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def audiences(self) -> typing.List[builtins.str]:
        '''List of audiences that can appear in the external token.

        This specifies what should be accepted in the ``aud`` claim of incoming tokens.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#audiences ApplicationFederatedIdentityCredential#audiences}
        '''
        result = self._values.get("audiences")
        assert result is not None, "Required property 'audiences' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''A unique display name for the federated identity credential.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#display_name ApplicationFederatedIdentityCredential#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def issuer(self) -> builtins.str:
        '''The URL of the external identity provider, which must match the issuer claim of the external token being exchanged.

        The combination of the values of issuer and subject must be unique on the app.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#issuer ApplicationFederatedIdentityCredential#issuer}
        '''
        result = self._values.get("issuer")
        assert result is not None, "Required property 'issuer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subject(self) -> builtins.str:
        '''The identifier of the external software workload within the external identity provider.

        The combination of issuer and subject must be unique on the app.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#subject ApplicationFederatedIdentityCredential#subject}
        '''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_id(self) -> typing.Optional[builtins.str]:
        '''The resource ID of the application for which this federated identity credential should be created.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#application_id ApplicationFederatedIdentityCredential#application_id}
        '''
        result = self._values.get("application_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_object_id(self) -> typing.Optional[builtins.str]:
        '''The object ID of the application for which this federated identity credential should be created.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#application_object_id ApplicationFederatedIdentityCredential#application_object_id}
        '''
        result = self._values.get("application_object_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the federated identity credential.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#description ApplicationFederatedIdentityCredential#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#id ApplicationFederatedIdentityCredential#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["ApplicationFederatedIdentityCredentialTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#timeouts ApplicationFederatedIdentityCredential#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ApplicationFederatedIdentityCredentialTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationFederatedIdentityCredentialConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.applicationFederatedIdentityCredential.ApplicationFederatedIdentityCredentialTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ApplicationFederatedIdentityCredentialTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#create ApplicationFederatedIdentityCredential#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#delete ApplicationFederatedIdentityCredential#delete}.
        :param read: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#read ApplicationFederatedIdentityCredential#read}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#update ApplicationFederatedIdentityCredential#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4d886c0c000a0568eaee11491ebfc161c5c24fc4fdb9e35d22ee2182aadd864)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#create ApplicationFederatedIdentityCredential#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#delete ApplicationFederatedIdentityCredential#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#read ApplicationFederatedIdentityCredential#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azuread/2.53.1/docs/resources/application_federated_identity_credential#update ApplicationFederatedIdentityCredential#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationFederatedIdentityCredentialTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationFederatedIdentityCredentialTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.applicationFederatedIdentityCredential.ApplicationFederatedIdentityCredentialTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdb20821f8aaf40aaf39fc70607c773751df5281b00218faf925f6606fd6beaf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76372561c2c6be4bc9e9e5e0bcab370c4f130cba380c2a764b861592190183cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b29fe813ac0fa0214693570733d4e5805ea900f043846002841b497e84295f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__695eac8296c89ae377e2fb5dcc93012c0c1300aafb9a31cff5ddd956a7d81e3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3bc96f5e43089722b82b03d183ce3c8e743b9200a628ce0c325a7f4689e255e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationFederatedIdentityCredentialTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationFederatedIdentityCredentialTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationFederatedIdentityCredentialTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1592d876ad835b7d8f8672a21f8fb1b0d90265da2ac5504b38bc02488592b54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApplicationFederatedIdentityCredential",
    "ApplicationFederatedIdentityCredentialConfig",
    "ApplicationFederatedIdentityCredentialTimeouts",
    "ApplicationFederatedIdentityCredentialTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__25e7d867a9c90dd50d1c04323bf335c3ebc4b1f16da64e62094a4e1357724a72(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    audiences: typing.Sequence[builtins.str],
    display_name: builtins.str,
    issuer: builtins.str,
    subject: builtins.str,
    application_id: typing.Optional[builtins.str] = None,
    application_object_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[ApplicationFederatedIdentityCredentialTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__111b1a919c696bc3efee258450c5965254c3e70e0547684e1117880b953b089f(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc1bbf78a3d6b6b79a10ff480fe2806af9d9302f1f60524758ae81f1a6c9e529(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfd1680fb38a49dafdede89fce7461301d9ddd1cdb08bc4828970fee0f01927e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7fb37025ae1dfd2127ce740fc31e7b87a02fddb657e0a1b12f2be5da85c63de(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cec3c9e74e1c495e2549c561369e2a01ff51cce2f53160f37f5b4ceb9a45a05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c18811a40e13ac2a450068f666e9a3f8589f90fcbe9f0762da8af397b3aa065(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ac30bffc1397fb5ecb505928adf40c5948a3c2a94154764b207801188bc4ce2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cf69a291e80b5188a723380593f321438c646649363cc41a16935d714eb4f40(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb4d7a5e18eeea9742686c92baaaa5a0717c636145e10208a5700c279ca730ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdfc444dacef508005ea0cec487aaa3d820cafcee1a9771fd65224d8369e8236(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    audiences: typing.Sequence[builtins.str],
    display_name: builtins.str,
    issuer: builtins.str,
    subject: builtins.str,
    application_id: typing.Optional[builtins.str] = None,
    application_object_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[ApplicationFederatedIdentityCredentialTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4d886c0c000a0568eaee11491ebfc161c5c24fc4fdb9e35d22ee2182aadd864(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdb20821f8aaf40aaf39fc70607c773751df5281b00218faf925f6606fd6beaf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76372561c2c6be4bc9e9e5e0bcab370c4f130cba380c2a764b861592190183cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b29fe813ac0fa0214693570733d4e5805ea900f043846002841b497e84295f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__695eac8296c89ae377e2fb5dcc93012c0c1300aafb9a31cff5ddd956a7d81e3e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3bc96f5e43089722b82b03d183ce3c8e743b9200a628ce0c325a7f4689e255e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1592d876ad835b7d8f8672a21f8fb1b0d90265da2ac5504b38bc02488592b54(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationFederatedIdentityCredentialTimeouts]],
) -> None:
    """Type checking stubs"""
    pass
