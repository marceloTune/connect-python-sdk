# CreateCustomerCardResponse
> squareconnect.models.create_customer_card_response

### Description

Defines the fields that are included in the response body of a request to the [CreateCustomerCard](#endpoint-createcustomercard) endpoint.  One of `errors` or `card` is present in a given response (never both).

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | [optional] 
**card** | [**Card**](Card.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


