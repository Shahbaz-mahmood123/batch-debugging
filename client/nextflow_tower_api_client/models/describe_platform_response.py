from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_batch_platform_metainfo import AwsBatchPlatformMetainfo
    from ..models.google_platform_metainfo import GooglePlatformMetainfo


T = TypeVar("T", bound="DescribePlatformResponse")


@_attrs_define
class DescribePlatformResponse:
    """
    Attributes:
        metainfo (Union['AwsBatchPlatformMetainfo', 'GooglePlatformMetainfo', Unset]):
    """

    metainfo: Union["AwsBatchPlatformMetainfo", "GooglePlatformMetainfo", Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.aws_batch_platform_metainfo import AwsBatchPlatformMetainfo

        metainfo: Union[Dict[str, Any], Unset]
        if isinstance(self.metainfo, Unset):
            metainfo = UNSET

        elif isinstance(self.metainfo, AwsBatchPlatformMetainfo):
            metainfo = self.metainfo.to_dict()

        else:
            metainfo = self.metainfo.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metainfo is not UNSET:
            field_dict["metainfo"] = metainfo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aws_batch_platform_metainfo import AwsBatchPlatformMetainfo
        from ..models.google_platform_metainfo import GooglePlatformMetainfo

        d = src_dict.copy()

        def _parse_metainfo(data: object) -> Union["AwsBatchPlatformMetainfo", "GooglePlatformMetainfo", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_platform_metainfo_type_0 = AwsBatchPlatformMetainfo.from_dict(data)

                return componentsschemas_platform_metainfo_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_platform_metainfo_type_1 = GooglePlatformMetainfo.from_dict(data)

            return componentsschemas_platform_metainfo_type_1

        metainfo = _parse_metainfo(d.pop("metainfo", UNSET))

        describe_platform_response = cls(
            metainfo=metainfo,
        )

        describe_platform_response.additional_properties = d
        return describe_platform_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
