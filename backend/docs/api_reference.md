# API Reference

## Resource types

### UserFullInfo

```json
{
    "id": 4, // integer
    "username":"alex", // string user name
    "display_name":"Алексей", // name that will be displayed, default value is username
    "password_hash":"...", // binary
    "email":"example@gmail.com", // string
    "is_active":true, // bool
    "created_at":"20/05/2025, 15:20:56" // string
}
```

### UserInfo

```json
{
    "id": 4, // integer
    "username":"alex", // string user name
    "display_name":"Алексей", // name that will be displayed, default value is username
    "is_active":true, // bool
    "created_at":"20/05/2025, 15:20:56" // string
}
```

### AuthToken

```json
{
    "user_id":1, // int
    "created_at":1289278117823, // int
    "expires_at":1289278117823 // int
}
```

## Urls

All urls are relative `http://localhost`

|Method|Url|Description|Args|
|-|-|-|-|
|**GET**|`/users/user`|Returns `UserInfo` resource.|`user_id: int`|
|**POST**|`/users/user`|Creates and returns `UserFullInfo` resource.|`username: string, display_name: string (optional), password: string, email: string`|
|**POST**|`/auth/login`|Logins and returns encoded `AuthToken` resource.|`email: string, password: string`|