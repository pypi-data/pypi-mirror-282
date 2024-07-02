# Gemnify SDK Python
A python based SDK developed for interacting with Gemnify

# Pip Install

The SDK can be installed via pip:

`pip install gemnify-sdk`

# Requirements
Developed using:

`python=3.11.9`

# Example Scripts
There are several example scripts which can be run and can be found in [example scripts](https://github.com/GMX-For-NFT/gemnify-sdk-python/tree/main/example_scripts). These are mostly for demonstration purposes on how to utilise the SDK, and can should be incoporated into your own scripts and strategies.



# General Usage

## Mock Token

now contract has been deployed on arbitrum sepolia, and mock stable coins are 
```
  "usdt": "0xeF0339A533E68f920444a3BB576669871Ce54c29",
  "usdc": "0x2f2F7Aa330Ef17019A9cB086da0970470fFe5a8c",
  "usde": "0x3c3ac50dc87d549609a238E287666C82E4bCBA6F",
  "fdusd": "0xc8E2ace39233FA977c7F388f31b4f232DAc647A2",
  "dai": "0x254b40Ce47F7DA1867e594613D08a23E198d7FE7"
```
decimal of all tokens is 18

if you want to get the test token, can directly mint on the testnet explorer
, or use the [example](https://github.com/GMX-For-NFT/gemnify-sdk-python/blob/main/example_scripts/liquidity.py#L19)
```python
util.mint_token(usdc_address, amount, receiver)
```

## Liquidity
[example](https://github.com/GMX-For-NFT/gemnify-sdk-python/blob/main/example_scripts/liquidity.py)
### Add Liquidity
```python
liquidity.add_liquidity(
    token, 
    amount,
    min_usdg,
    min_ulp  
)
```

- `token`  type str, token address, eg: dai address
- `amount` type int, token amount to deposit
- `min_usdg` type int, minimum acceptable USDG value of the ULP purchased
- `min_ulp` type int, minimum acceptable ULP amount

before add liquidity, should approve token to `UlpManager` first

```python
util.approve_token_to_ulp_manager(token_address, amount)
```

### Remove Liquidity
```python
liquidity.remove_liquidity(
    ulp_amount,  
    min_out,      
    receiver,  
)
```
- `ulp_amount`  type int, the amount of ULP to remove, decimal is 18
- `min_out`  type int, the minimum acceptable amount of tokens to be received
- `receiver`  type str, the address to receive tokens

### Get AmountOut When Remove Liquidity
when remove liquidity, users can receive all tokens of the stable tokens proportionally， this interface returns the amount of each token
```python
liquidity.get_tokens_amount_out(
    ulp_amount
)
```
return is array:
- token name
- token amount out
- token amount out with formatting precision

### Get Claimable Reward
get claimable reward usdc
```python
liquidity.get_claimable(user)
```

### Claim Reward
claim reward usdc
```python
liquidity.handleRewards()
```

### Get User ULP
get deposited ULP of specific user
```python
liquidity.get_user_ulp(
    user,
    ulp_address
)
```
- `user` user address
- `ulp_address`, ulp address, can get from `util.get_token_address("ulp")`

return:
- ulp amount, decimal is 18

### Get Total ULP
get total deposited ULP
```python
liquidity.get_total_ulp(
    ulp_address
)
```
- `ulp_address` ulp address, can get from `util.get_token_address("ulp")`

return:
- ulp amount, decimal is 18

## Position
[example](https://github.com/GMX-For-NFT/gemnify-sdk-python/blob/main/example_scripts/position.py)

### Increase Long or Short Position
user's request to open a position
```python
position.create_increase_position(
    index_token,
    amount_in,
    size_delta,
    is_long,
    acceptable_price,
    execution_fee,
    callback_target
    value = val,
) 
```
- `index_token` type str, the address of token you want to long or short, eg, dai address
- `amount_in` type int, the amount of token you want to deposit as collateral
- `size_delta` type int, the USD value of the change in position size, decimal is 30
- `is_long` type bool, is position long or short? (long->true,short->false)
- `acceptable_price` type int, the price acceptable when executing the request, decimal is 30. (if long, > market price, if short, < market price)
- `execution_fee` type int,  execution_fee >= `position.get_min_execution_fee`, setting on arbitrum sepolia is 0.0001 eth
- `callback_target` type string, an optional callback contract, this contract will be called on request execution or cancellation
- `value` type int, = execution_fee

before call `create_increase_position`, should:
1. approve plugin, it only needs to be called once the first time to open position, and does not need to be done again afterward
```python
util.approve_plugin_position_router()
```
2. approve usdc to router,
```python
util.approve_token_to_router(
    usdc_address, 
    amount
)
```

### Decrease Long or Short Position
user's request to decrease a position
```python
position.create_decrease_position(
    index_token,
    collateral_delta,
    size_delta,
    is_long,
    receiver,
    acceptable_price,
    execution_fee,
    callback_target,
    value = val
) 
```

- `index_token`  type str, the address of token you want to long or short
- `collateral_delta` type int, the amount of collateral in USD value to withdraw, if decrease max position, set 0. decimal is 30
- `size_delta` type int, the USD value of the change in position size, decimal is 30
- `is_long` type bool, is position long or short?(long->true,short->false)
- `receiver` type str, the address that receive the token after decrease the position 
- `acceptable_price` type int, the price acceptable when executing the request, decimal is 30. (if long, < market price, if short, > market price)
- `execution_fee` type int, execution_fee >= `position.get_min_execution_fee`
- `callback_target`type str
- `value` type int,  = execution_fee


### Add Collateral

use `position.create_increase_position`, and set size_delta to 0

### Remove Collateral

use `position.create_decrease_position`, and set size_delta to 0

### Get Position

```python
position.get_position(
    user_address,
    collateral_token,
    index_token,
    is_long
)
```
- `user_address` type str
- `collateral_token` type str, usdc address
- `index_token`, type str, the address of token has been long or short
- `is_long` type bool

return value:
```python
(
    size,
    collateral,
    average_price,
    entry_borrowing_rate,
    funding_fee_amount_per_size,
    claimable_funding_amount_per_size,
    reserve_amount, 
    realised_pnl, 
    last_increased_time
)
```

## Order
[example](https://github.com/GMX-For-NFT/gemnify-sdk-python/blob/main/example_scripts/order.py)

### Create Increase Order

```python
order.create_increase_order(
    amount_in,
    index_token,
    size_delta,
    collateral_token,
    is_long,
    trigger_price,
    trigger_above_threshold,
    execution_fee,
    value=val
)
```
- `amount_in` type int, the amount of token you want to deposit as collateral
- `index_token` type str, the address of token you want to long or short
- `size_delta` type int, the USD value of the change in position size, decimal is 30
- `collateral_token` type str, usdc address
- `is_long` type bool, is position long or short?(long->true,short->false)
- `trigger_price` type int, the trigger price for the position, decimal is 30 
- `trigger_above_threshold` type bool, when executing order if need market price < trigger_price, set false or if need market price > _trigger_price, set true
- `execution_fee`, type int,   >= `order.get_min_execution_fee`
- `value` type int,  = execution_fee

`trigger_price`/`trigger_above_threshold` should be set as:
- if position is long:
    - is_long: true
    - trigger_price: < current market price
    - triggerAboveThreshold: false
- if position is short:
    - is_long: false
    - trigger_price: > current market price
    - triggerAboveThreshold: true
  

before call `create_increase_order`, should:
1. approve plugin, it only needs to be called once the first time to create order, and does not need to be done again afterward
```python
util.approve_plugin_order_book()
```
2. approve usdc to router,
```python
util.approve_token_to_router(
    usdc_address, # usdc
    amount
)
```

### Update Increase Order

```python
order.update_increase_order(
    order_index,
    size_delta,
    trigger_price,
    trigger_above_threshold
)
```

- `order_index` type int, the index of the order
- `size_delta` type int, size of order after update
- `trigger_price` type int, the trigger price after update
- `trigger_above_threshold` type bool, trigger_above_threshold after update

### Cancel Increase Order

```python
order.cancel_increase_order(
    order_index
)
```
- `order_index` type int, the index of the order


### Get Increase Order Index
get user's latest increase order index
```python
order.get_increase_order_index(
    user_address
)
```

### Get Increase Order
get user's increase order info by order index
```python
order.get_increase_order(
    user_address,
    order_index
)
```

returns
- token 
- token_amount
- collateral_token, usdc
- index_token,
- size_delta,
- is_long
- trigger_price
- trigger_above_threshold
- execution_fee

### Create Decrease Order
```python
order.create_decrease_order(
    index_token,
    size_delta,
    collateral_token,
    collateral_delta,
    is_long,
    trigger_price,
    trigger_above_threshold,
    value=val
) 
```

- `index_token` type str, the address of token you want to long or short
- `size_delta` type int, the USD value of the change in position size, decimal is 30
- `collateral_token` type str, usdc address
- `collateral_delta` type int, the amount of collateral in USD value to withdraw, decimal is 30
- `is_long` type bool, is position long or short?(long->true,short->false)
- `trigger_price` type int, the trigger price for the position, decimal is 30 
- `trigger_above_threshold` type int
- `value` type int, >= `order.get_min_execution_fee`

`trigger_price`/`trigger_above_threshold` should be set as:

- if position is long:
  - TP(take profit):
    - is_long: true
    - trigger_price: > current market price
    - triggerAboveThreshold: true 
  - SL(stop loss):
    - is_long: true 
    - trigger_price: < current market price
    - trigger_above_threshold: false 
- if position is short:
  - TP:
    - is_long: false 
    - trigger_price: < current market price
    - trigger_above_threshold: false 
  - SL:
    - is_long: false
    - trigger_price: > current market price 
    - trigger_above_threshold: true

### Update Decrease Order
```python
order.update_decrease_order(
   order_index,
   collateral_delta,
   size_delta,
   trigger_price,
   trigger_above_threshold
) 
```

- `order_index` type int, the index of the order
- `collateral_delta` type int, size of position after update
- `size_delta` type int, size of order after update
- `trigger_price` type int, the trigger price after update
- `trigger_above_threshold` type bool trigger_above_threshold after update


### Cancel Decrease Order

```python
order.cancel_decrease_order(
    order_index 
)
```

- `order_index` the index of the order

### Get Decrease Order Index
get user's latest decrease order index
```python
order.get_decrease_order_index(
    user_address
)
```

### Get Decrease Order
get user's decrease order info by order index
```python
order.get_decrease_order(
    user_address,
    order_index
)
```

return struct is same as `order.get_increase_order`

### Cancel Multiple Order
cancel multiple order
```python
order.cancel_multiple(
    swap_order_indexes,
    increase_order_indexes,
    decrease_order_indexes
) 
```

- `swap_order_indexes`  the index array of swap order 
- `increase_order_indexes` the index array of increase order 
- `decrease_order_indexes` the index array of decrease order


## Swap
[example](https://github.com/GMX-For-NFT/gemnify-sdk-python/blob/main/example_scripts/swap.py)

```python
swap.swap(
    path,
    amount_in,
    min_out,
    receiver
)
```

- `path` type array, if swap A to B, _path is [A, B]
- `amount_in` type int, amount of token in to swap
- `min_out` type int, min amount of token out
- `receiver` type str

before swap, should approve to router first
```python
util.approve_token_to_router(token_address, amount)
```

## Fee
[example](https://github.com/GMX-For-NFT/gemnify-sdk-python/blob/main/example_scripts/fee.py)


### Claim Funding Fee
claim funding fee
```python 
fee.claim_funding_fees()
```



### Get Funding Fee
get funding fee
```python
fee.get_funding_fee_amount(user_address)
```


### Get Price Impact Fee
get swap price impact fee
```python
fee.get_swap_price_impact_fee(
    token_in,
    token_out,
    token_amount
)
```

### Get Deposit  Fee
 get deposit fee basis point 
```python
fee.get_deposit_fee_basis_points(
   token_address,
   amount
)
```
- `token_address`  token to deposit
- `amount_in`  amount of token to deposit

return
- the first value is basic point of deposit fee, denominator is 10000
- the second value is balance reward


### Get Withdraw  Fee

```python
fee.get_withdraw_fee_basis_points(
  ulp_address,
  amount
)
```
- `ulp_address`  ulp address
- `amount`  amount of ulp to withdraw

return:
- basic point of withdraw fee, denominator is 10000  



### Get Swap Fee

```python
fee.get_swap_fee_basis_points(
    token_in,
    token_out,
    token_amount
)
```

### Get Borrowing Rates

```python
fee.get_borrowing_rates(
    token
)
```
- `token`, only usdc address

## Reader

[example](https://github.com/GMX-For-NFT/gemnify-sdk-python/blob/main/example_scripts/reader.py)

### Get Global OI
get global OI
```python
reader.get_global_OI()
```

returns:
- max global OI
- available global OI

### Get Aum
```python
reader.get_aum()
```

### Get Pool Info
```python
reader.get_pool_info(
    token_address
)
```

returns:
- pool_amount,  liquidity of this token in pool 
- reserved_amount
- buffer_amount
- global_long_size
- global_long_average_price
- global_short_size
- global_short_average_price
- usdg_amount