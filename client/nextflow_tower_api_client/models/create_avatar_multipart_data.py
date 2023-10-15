from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="CreateAvatarMultipartData")


@_attrs_define
class CreateAvatarMultipartData:
    """
    Attributes:
        image (Union[Unset, File]):
    """

    image: Union[Unset, File] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        image: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _image = d.pop("image", UNSET)
        image: Union[Unset, File]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = File(payload=BytesIO(_image))

        create_avatar_multipart_data = cls(
            image=image,
        )

        create_avatar_multipart_data.additional_properties = d
        return create_avatar_multipart_data

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
